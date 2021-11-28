from behave import *
from bdd_calculator import *


@given("I open the calculator")
def step_ipml(context):
    context.nesne1 = bdd_calc1()

@given("I entered {numb1:d}")
def step_ipml(context, numb1):
    context.nesne1 = bdd_calc1()
    context.nesne1.numb1 = numb1

@given("I entered {numb1:f}")
def step_ipml(context, numb1):
    context.nesne1 = bdd_calc1()
    context.nesne1.numb1 = numb1

@given("and {numb2:d} to the calculator")
def step_ipml(context, numb2):
    context.nesne1.numb2 = numb2

@given("I entered calculator type {calc_type}")
def step_ipml(context, calc_type):
    context.calc_type = calc_type

@given("I entered {equ1}")
def step_ipml(context, equ1):
    context.nesne1 = bdd_calc1()
    context.nesne1.equ1 = equ1

@when("the calculator shows the menu and the user inputs {type1}")
def step_impl(context, type1):
    context.nesne1.type1 = type1

@when("I press add")
def step_impl(context):
    context.result = context.nesne1.calc_sum()

@when("I press subtract")
def step_impl(context):
    context.result = context.nesne1.calc_subt()

@when("I press multiplication")
def step_impl(context):
    context.result = context.nesne1.calc_mult()

@when("I press division")
def step_impl(context):
    context.result = context.nesne1.calc_div()

@when("I press calculate")
def step_impl(context):
    context.result = context.nesne1.scientific_calculator()

@then("then the user selected the type")
def step_impl(context):
    assert context.nesne1.ask_for_type()

@then("the warning message is returned to the user")
def step_impl(context):
    assert context.nesne1.ask_for_type() == "Wrong Input"

@then("then the user selects {type1}")
def step_impl(context, result1):
    assert context.result == result1

@then("The result is {result1:d}")
def step_impl(context, result1):
    assert context.result == result1

@then("The result is {result1:f}")
def step_impl(context, result1):
    assert context.result == result1

@then("The result is {result1}")
def step_impl(context, result1):
    assert context.result == result1

@then("The user gets Zero Division Error")
def step_impl(context):
    assert context.result == "ZeroDivisionError"
