"""Launch Gradio UI and wire components."""
import gradio as gr
from api import answer_query
from utils import load_config


cfg = load_config()


with gr.Blocks() as demo:
gr.Markdown("# Farmeasy 2.0 — Farmer Query Assistant")
with gr.Row():
inp = gr.Textbox(lines=3, placeholder="Ask a farming question...", label="Question")
out = gr.Textbox(lines=10, label="Answer")
btn = gr.Button("Ask")


def _ask(q: str):
if not q:
return "Please enter a question."
return answer_query(q)


btn.click(_ask, inputs=inp, outputs=out)


if __name__ == "__main__":
demo.launch()
