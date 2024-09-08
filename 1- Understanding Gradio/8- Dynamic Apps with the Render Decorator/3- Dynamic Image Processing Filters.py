# In this example, users can upload an image and then dynamically apply different filters based on their selection. The number of filters is also adjustable.


import gradio as gr
from PIL import Image, ImageFilter

def apply_filter(image, filters):
    img = Image.open(image)
    for filter_name in filters:
        if filter_name == "BLUR":
            img = img.filter(ImageFilter.BLUR)
        elif filter_name == "CONTOUR":
            img = img.filter(ImageFilter.CONTOUR)
        elif filter_name == "DETAIL":
            img = img.filter(ImageFilter.DETAIL)
    return img

with gr.Blocks() as demo:
    num_filters = gr.State(1)  # Start with 1 filter
    filter_options = gr.CheckboxGroup(["BLUR", "CONTOUR", "DETAIL"], value=["BLUR"])
    
    @gr.render(inputs=[num_filters, filter_options])
    def render_filters(count, selected_filters):
        filters = []
        for i in range(count):
            checkbox = gr.Checkbox(label=f"Filter {i+1}", key=f"filter-{i}")
            filters.append(checkbox)
        
        def update_filters(*selected):
            return [filter_name for filter_name, checked in zip(selected_filters, selected) if checked]
        
        apply_btn = gr.Button("Apply Filters")
        output_image = gr.Image(label="Filtered Image")
        apply_btn.click(apply_filter, inputs=[gr.File(), set(filters)], outputs=output_image)

    add_filter_btn = gr.Button("Add Filter")
    remove_filter_btn = gr.Button("Remove Filter")
    add_filter_btn.click(lambda x: x + 1, num_filters, num_filters)
    remove_filter_btn.click(lambda x: max(x - 1, 1), num_filters, num_filters)

demo.launch()
