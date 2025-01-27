import torch
from conf.config import config
from src.logger.logger import logger
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread

device = "cuda" if torch.cuda.is_available() else "cpu"


class LLMClient:
    def __init__(self, model_name):
        self.model_name = model_name
        self.model_path = config["LLM"][model_name]["path"]

    def load_model(self):
        pass

    def __call__(self, sys_prompt, user_prompt):
        pass


class QwenClient(LLMClient):
    def __init__(self, model_name):
        super().__init__(model_name)
        self.tokenizer = None
        self.model = None
        logger.info("初始化LLM")
        self.load_model()

    def load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_path, torch_dtype="auto").to(device)
        logger.info(f"加载模型：{self.model_name}")
        if device == "cpu":
            logger.warning("当前LLM加载设备为CPU，生成速度会比较慢")

    def __call__(self, sys_prompt, user_prompt, stream=False):
        messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt}
        ]
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
        if not stream:
            generated_ids = self.model.generate(
                **model_inputs,
                max_new_tokens=512,
            )
            generated_ids = [
                output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
            ]
            response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

            return response
        else:
            streamer = TextIteratorStreamer(self.tokenizer, skip_prompt=True, skip_special_tokens=True)
            generation_kwargs = dict(model_inputs, streamer=streamer, max_new_tokens=512)
            thread = Thread(target=self.model.generate, kwargs=generation_kwargs)
            thread.start()

            return streamer
