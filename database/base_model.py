
class Model:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def string(self, length):
        return 'VARCHAR ({})'.format(length)

    @classmethod
    def integer(self):
        return 'INTEGER'

    @classmethod
    def boolean(self, default=False):
        return 'BOOLEAN DEFAULT {}'.format(default)

    @classmethod
    def text(self):
        return 'TEXT'

    @classmethod
    def datetime(self):
        return 'TIMESTAMP'

    @classmethod
    def unique(self):
        return 'UNIQUE'

    @classmethod
    def serial(self):
        return 'SERIAL'

    @classmethod
    def numeric(self):
        return 'numeric'

    @classmethod
    def primary(self):
        return 'PRIMARY KEY'

    @classmethod
    def not_null(self, val=True):
        return 'NOT NULL' if val else 'NULL'

    @classmethod
    def foreignkey(self, ref, on_delete_cascade=True):
        cascade = 'ON DELETE CASCADE' if on_delete_cascade \
            else 'ON DELETE RESTRICT'
        table, column = ref.split('.')
        return 'REFERENCES {}({}) {}'.format(
            table,
            column,
            cascade)

    @classmethod
    def create(cls):
        string = '''CREATE TABLE IF NOT EXISTS {} ({}{})'''.format(
            cls.__name__.lower(),
            ','.join([i for i in cls.parse_fields().values()]),
            cls.format_meta())
        return string

    @classmethod
    def format_meta(cls):
        if getattr(cls, '_Meta_', None):
            return ', UNIQUE({})'.format(','.join(cls._Meta_.unique_together))
        return ''

    @classmethod
    def parse_fields(cls):
        dict1 = {key: key+' '+' '.join(value) for (key, value)
                 in cls.__dict__.items() if key[:1] != '_' or not isinstance(value, object)}
        return dict1

    @classmethod
    def fields(cls, *args, **kwargs):
        return args

    def process_records(self, records):
        if type(records) is list:
            values = [str(tuple(record.values())) for record in records]
            values = ', '.join(values)

            columns = records[0].keys()
        else:
            values = tuple(records.values())
            columns = records.keys()
        return columns, values

    def insert_query(self, records):
        columns, values = self.process_records(records)
        record = {
            'table_name': self.__class__.__name__.lower(),
            'columns': ','.join(columns),
            'values': values
        }
        return '''INSERT INTO {table_name}({columns}) VALUES {values} RETURNING *'''.format(**record)

    @classmethod
    def find(cls, operator, **kwargs):
        record = {
            'table_name': cls.__name__.lower(),
            'columns': ','.join(cls.parse_fields().keys()),
            'number': 1000,
            'params': cls.get_kwargs(operator, **kwargs) if kwargs else ''
        }
        return'''SELECT {columns} from {table_name} {params} LIMIT {number} '''.format(**record)

    @classmethod
    def get_kwargs(cls, operator, **kwargs):
        operator = " " + operator + " "
        query = []
        for key, value in kwargs.items():
            if type(value) is int:
                query.append(f"{key}={value}")
            else:
                query.append(f"{key}='{value}'")
        return " WHERE "+operator.join(query)
