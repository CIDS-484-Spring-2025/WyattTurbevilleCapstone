class EnumManager:
    def __init__(self):
        self._table_enums = {
            'Test': {
                'testType': ['BAP', 'MAC', 'Catalase', 'GramStain', 'Prototheca']
            },
            'Sample': {
                'Quarter': ['LR', 'LF', 'RR', 'RF', 'C']
            },
            'MAC': {
                'Lactose': ['positive', 'negative', 'dry', 'wet', 'mucoid'],
                'TSI': ['AA', 'AK', 'KK', 'KA', 'G', 'S']
            },
            'BAP': {
                'xhem': ['nhem', 'bhem', 'ahem'],
                'size': ['tiny', 'small', 'medium', 'large']
            }
        }

    def get_table_choices(self, table_name):
        """
        Get all ENUM choices for a specific table
        Returns: {'column1': [(value, label)], 'column2': [(value, label)]}
        """
        if table_name not in self._table_enums:
            raise ValueError(f"Table '{table_name}' not found in ENUM registry")
        
        return {
            column: [(v, v) for v in values]
            for column, values in self._table_enums[table_name].items()
        }
    
    def get_column_choices(self, table_name, column_name):
        """
        Get choices for a specific column in a table
        Returns: [(value, label)]
        """
        table = self._table_enums.get(table_name, {})
        return [(v, v) for v in table[column_name]]