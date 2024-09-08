def process_payment(payment_info):
    gr.Info("Processing payment...")
    if not payment_info.get("card_number"):
        raise gr.Error("Credit card number is missing.")
    if not payment_info.get("expiry_date"):
        gr.Warning("Expiry date is missing, using default.")
    gr.Info("Payment processed successfully.")
