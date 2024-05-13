from django.shortcuts import render
from forex_python.converter import CurrencyRates

def convert_currency(request):
    if request.method == 'POST':
        base_currency = request.POST.get('base_currency')
        target_currency = request.POST.get('target_currency')
        amount = float(request.POST.get('amount', 0))  # Default to 0 if amount is not provided

        if base_currency and target_currency:
            c = CurrencyRates()
            rate = c.get_rate(base_currency, target_currency)
            converted_amount = amount * rate
            return render(request, 'converter.html', {'converted_amount': converted_amount})

    return render(request, 'converter.html')
