import gradio as gr

google_analytics_id = 'YOUR_TRACKING_ID'

head = f"""
<script async src="https://www.googletagmanager.com/gtag/js?id={google_analytics_id}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag() {{ dataLayer.push(arguments); }}
  gtag('js', new Date());
  gtag('config', '{google_analytics_id}');
</script>
"""

with gr.Blocks(head=head) as demo:
    gr.Textbox(placeholder="Enter your feedback...")
    
demo.launch()
