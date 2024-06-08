import p2
while True:
        expression = input("Enter the expression: ")
        format_choice = input("Enter the format (infix/postfix/prefix): ")
        action = input("Convert or Evaluate? (convert/evaluate): ")

        if action == 'convert':
            if format_choice == 'infix':
                new_format = input("Enter the format to convert to (postfix/prefix): ")
                if new_format == 'postfix':
                    result = p2.intopost(expression)
                elif new_format == 'prefix':
                    result = p2.intopre(expression)
            elif format_choice == 'postfix':
                new_format = input("Enter the format to convert to (infix/prefix): ")
                if new_format == 'infix':
                    result = p2.posttoin(expression)
                elif new_format == 'prefix':
                    result = p2.posttopre(expression)
            elif format_choice == 'prefix':
                new_format = input("Enter the format to convert to (infix/postfix): ")
                if new_format == 'infix':
                    result = p2.pretoin(expression)
                elif new_format == 'postfix':
                    result = p2.pretopost(expression)
            print("Result:", result)
        elif action == 'evaluate':
            result = p2.evaluate(expression,format_choice)
            print("Result:", result)
        else:
            print("Invalid action. Please choose 'convert' or 'evaluate'.")

        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            print("Exiting...")
            break



