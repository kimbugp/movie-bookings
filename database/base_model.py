
class Model:

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
    def datetime(self, auto_add=False):
        string = 'TIMESTAMP'
        return string+' DEFAULT NOW()' if auto_add else string

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
    def time(self):
        return 'TIME '

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
        dict1 = {cls.__name__.lower()+'.'+key: key+' '+' '.join(value) for (key, value)
                 in cls.__dict__.items() if key[:1] != '_' and not callable(value)}
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
    def find(cls, operator, joins='', check='=', **kwargs):
        table = cls.__name__.lower()
        record = {
            'table_name': table,
            'columns': ','.join(cls.parse_fields().keys()),
            'number': 1000,
            'params': cls.get_kwargs(operator, check, **kwargs) if kwargs else '',
            'joins': joins}
        return'''SELECT distinct * from {table_name} {joins} {params} LIMIT {number} '''.format(**record)

    @classmethod
    def update(cls, id, operator, **kwargs):
        table = cls.__name__.lower()
        record = {
            'table_name': table,
            'columns': ','.join(cls.parse_fields().keys()),
            'params': f'WHERE {table}.id = {id}',
            'values': ', '.join(cls.parse_values(kwargs, update=True))
        }
        return'''UPDATE {table_name}  SET {values} {params} RETURNING * '''.format(**record)

    @classmethod
    def get_kwargs(cls, operator, check='=', **kwargs):
        operator = " " + operator + " "
        query = cls.parse_values(kwargs, check)
        return " WHERE "+operator.join(query)

    @classmethod
    def parse_values(cls, kwargs, check='=', update=False):
        table = cls.__name__.lower()+'.'
        if update:
            table = ''
        query = []
        for key, value in kwargs.items():
            if type(value) is int:
                query.append(f"{table}{key}{check}{value}")
            elif type(value) is dict:
                query.append(
                    f"{value.get('table')}.{key}{check}'{value.get('value')}'")
            else:
                query.append(f"{table}{key}{check}'{value}'")
        return query
