class Model:

    @classmethod
    def string(self, length):
        return 'VARCHAR ({})'.format(length)

    @classmethod
    def integer(self):
        return 'INTEGER'

    @classmethod
    def text(self):
        return 'TEXT'

    @classmethod
    def date(self):
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
        cascade = 'ON DELETE CASCADE' if on_delete_cascade else 'ON DELETE RESTRICT'
        table, column = ref.split('.')
        return 'REFERENCES {}({}) {}'.format(
            table,
            column,
            cascade)

    @classmethod
    def create(cls):
        string = '''CREATE TABLE IF NOT EXISTS {} ({})'''.format(
            cls.__name__.lower(),
            ','.join([i for i in cls.parse_fields().values()]))

        return string

    @classmethod
    def parse_fields(cls):
        dict1 = {key: key+' '+' '.join(value) for (key, value)
                 in cls.__dict__.items() if key[:1] != '_'}
        return dict1

    @classmethod
    def fields(cls, *args, **kwargs):
        return args

    def insert(self, record):
        record = {
            'table_name': self.__class__.__name__.lower(),
            'columns': ','.join(record.keys()),
            'values': ','.join(record.values())
        }
        return '''INSERT INTO {table_name}({columns}) VALUES ({values})'''.format(**record)

    @classmethod
    def find(cls, operator, **kwargs):
        record = {
            'table_name': cls.__name__.lower(),
            'columns': ','.join(cls.parse_fields().keys()),
            'number': 1000,
            'params': cls.get_kwargs(operator, **kwargs) if kwargs else ''
        }
        return'''SELECT {columns} from {table_name} LIMIT {number} {params}'''.format(**record)

    @classmethod
    def get_kwargs(cls, operator, **kwargs):
        operator = " " + operator + " "
        ls = []
        for key, value in kwargs.items():
            ls.append(key+'='+str(value))
        return " WHERE "+operator.join(ls)

    # update method
    # get by id
    # get by kwargs
    # delete
    # join method
