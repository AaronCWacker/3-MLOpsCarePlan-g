import gradio as gr

context = "What should be documented in a care plan?\n"
context = context + "Regardless of what your preferences are, your care plan should include:\n"
context = context + "What your assessed care needs are.\n"
context = context + "What type of support you should receive.\n"
context = context + "Your desired outcomes.\n"
context = context + "Who should provide care.\n"
context = context + "When care and support should be provided.\n"
context = context + "Records of care provided.\n"
context = context + "Your wishes and personal preferences.\n"
context = context + "The costs of the services.\n"

context = context + "Dimensions\n"
context = context + "1-Ontology of Plan\n"
context = context + "2-Problems as evidenced by Signs of Systems\n"
context = context + "3-Assessment of Needs\n"
context = context + "4-Questions about problems faced\n"
context = context + "5-Goals for long and short term improvements\n"
context = context + "6-Knowledge-Behavior-Status Quality Measures\n"
context = context + "7-Intervention List of Options\n"
context = context + "8-Quality Measures\n"
context = context + "9-Pathways Available\n"

with open('WritingCarePlans.txt', 'r') as file:
        context = file.read()

question = "What should be documented in a care plan?"

gr.Interface.load(
             "huggingface/deepset/roberta-base-squad2",
             theme="default",
             css=".footer{display:none !important}",
             inputs=[gr.inputs.Textbox(lines=12, default=context, label="Context paragraph"), gr.inputs.Textbox(lines=3, default=question, label="Question")],
             outputs=[gr.outputs.Textbox(label="Answer"), gr.outputs.Textbox(label="Score")],
             title=None,
             description="Provide your own paragraph and ask any question about the text. How well does the model answer?").launch()

