from typing import Any
import sympy

def expr_formarted(entry_expression: str):
    expression = ""
    var_control = {}

    for i, element in enumerate(entry_expression): # refact expression
        expression += element
        if i < len(entry_expression) - 1:
            if (
                element in "+-*/()" and entry_expression[i+1].isdigit() or 
                element.isdigit() and entry_expression[i+1] in "+-*/()"
            ):
                expression += ' '
    
    for v in expression.split(): # var control
        if v.isalnum():
            var_control[v] = sympy.Symbol(v)

    expression = sympy.parse_expr(expression, var_control) # add vars symbols im expression
    return expression


def expr_latex(entry_expression: sympy.Expr | Any):
    return sympy.latex(entry_expression)


def resolver(entry_expression: str, mode: int = 1):
    expression = expr_formarted(entry_expression)
    answer = sympy.expand(expression) if mode != 2 else sympy.factor(expression)
    return sympy.latex(answer)
    
    
if __name__ == "__main__":
    pass

