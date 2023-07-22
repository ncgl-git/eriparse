from typing import Any, Dict


def generate_test_framework(results: Dict[str, Any]):
    for name, value in results.items():
        cleaned_name = name.lower().replace(" ", "_").rstrip(":").replace("(", "").replace(")", "")
        test_name = f"test_{cleaned_name}"

        print(
            (
                f"""
                   def {test_name}(self):
                       result = parse(self.soup)

                       self.assertEqual(
                            '{value}',
                            result['{name}']
                        )
                   """
            )
        )
