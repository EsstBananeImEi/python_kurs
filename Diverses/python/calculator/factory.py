from calculator import Calculator


class Factory:

    @staticmethod
    def operator_factory(operator: str):
        match operator:
            case "+": return Calculator.addiere
            case "-": return Calculator.substrahiere
            case "*": return Calculator.multipliziere
            case "/": return Calculator.dividiere
            case _: return "Operator nicht gefunden"
