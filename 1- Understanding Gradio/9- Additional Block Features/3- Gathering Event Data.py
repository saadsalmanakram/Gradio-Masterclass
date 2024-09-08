# This example demonstrates how to use gr.SelectData to show details about the selected option in a Dropdown menu and the specific cell selected in a DataFrame.

import gradio as gr

# Dropdown Selection Example
def show_dropdown_selection(select_evt: gr.SelectData):
    return f"Selected option: {select_evt.value} at index {select_evt.index}"

with gr.Blocks() as demo:
    dropdown = gr.Dropdown(["Option 1", "Option 2", "Option 3"], label="Choose an Option")
    selected_option = gr.Textbox()

    dropdown.select(show_dropdown_selection, None, selected_option)

# DataFrame Selection Example
def mark_cell(data: list[list[str]], cell_value: str, evt: gr.SelectData):
    if data[evt.index[0]][evt.index[1]] == "":
        data[evt.index[0]][evt.index[1]] = cell_value
    return data

with gr.Blocks() as demo:
    cell_value = gr.Textbox("X", label="Mark Cell")
    table = gr.Dataframe(value=[["", "", ""] for _ in range(3)], interactive=True, type="array")

    table.select(mark_cell, [table, cell_value], [table])

if __name__ == "__main__":
    demo.launch()
