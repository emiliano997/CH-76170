from openpyxl import load_workbook

def copy_excel_file(input_file, output_file):
  """
  This function loads an Excel workbook from a specified input file and saves it with a different name to an output file.

  Parameters:
  input_file (str): The path and name of the input Excel file.
  output_file (str): The path and name of the output Excel file.
  """
  # Load the workbook
  workbook = load_workbook(input_file)

  # Save the workbook with a different name
  workbook.save(output_file)

# Example usage
if __name__ == "__main__":
  input_file = 'example.xlsx'
  output_file = 'output.xlsx'
  copy_excel_file(input_file, output_file)


