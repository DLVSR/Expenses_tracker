from django.shortcuts import render, redirect
from .models import Expense
from django.db.models import Sum, Count
from datetime import date # Import the date module

def expense_tracker_view(request):
    # The POST handling logic remains the same
    if request.method == 'POST':
        # ... (no changes needed here)
        if 'delete_id' in request.POST:
            expense_id = request.POST.get('delete_id')
            try:
                expense_to_delete = Expense.objects.get(pk=expense_id)
                expense_to_delete.delete()
            except Expense.DoesNotExist:
                pass
        else:
            amount = request.POST.get('amount')
            category = request.POST.get('category')
            date_str = request.POST.get('date') # Renamed to avoid conflict
            if amount and category and date_str:
                Expense.objects.create(amount=amount, category=category, date=date_str)
        
        return redirect('expense_tracker')

    # This part handles the initial page load (GET request)
    expenses = Expense.objects.all().order_by('-date')

    # Calculate totals and breakdown
    total_expenses_data = expenses.aggregate(total=Sum('amount'))
    total_expenses = total_expenses_data['total'] if total_expenses_data['total'] else 0
    transaction_count = expenses.count()
    category_breakdown = expenses.values('category').annotate(total=Sum('amount')).order_by('-total')

    # --- NEW: Get today's date ---
    # Get the current date and format it as 'YYYY-MM-DD'
    todays_date = date.today().strftime('%Y-%m-%d')

    context = {
        'expenses': expenses,
        'total_expenses': total_expenses,
        'transaction_count': transaction_count,
        'category_breakdown': category_breakdown,
        'todays_date': todays_date, # Add it to the context
    }

    return render(request, 'index.html', context)