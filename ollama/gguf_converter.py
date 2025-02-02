from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "deepseek-ai/deepseek-r1-distill-qwen-7b"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("/root/.ollama/deepseek_r1_qwen7b_gguf")
tokenizer.save_pretrained("/root/.ollama/deepseek_r1_qwen7b_gguf")
