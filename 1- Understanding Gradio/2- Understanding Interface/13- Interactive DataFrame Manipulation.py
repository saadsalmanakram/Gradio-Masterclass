import gradio as gr
import pandas as pd

def filter_dataframe(df, column, threshold):
    filtered_df = df[df[column] > threshold]
    return filtered_df

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 22],
    "Score": [88.5, 92.3, 79.0, 85.4, 90.1]
}
df = pd.DataFrame(data)

demo = gr.Interface(
    fn=filter_dataframe,
    inputs=[
        gr.Dataframe(value=df, label="Input DataFrame", interactive=True),
        gr.Dropdown(choices=["Age", "Score"], label="Column to Filter"),
        gr.Number(label="Threshold Value")
    ],
    outputs=gr.Dataframe(label="Filtered DataFrame"),
    title="DataFrame Filter Tool",
    description="Filter the rows of a DataFrame based on a threshold for a selected column."
)

demo.launch()
