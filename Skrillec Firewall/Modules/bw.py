
class Get:
    def Command(OperatingSystem:str):
        match OperatingSystem:
            case "Windows":
                return "cls"

            case "Linux":
                return "clear"
            
            case "Darwin":
                return "clear"
            
            case _:
                return ""