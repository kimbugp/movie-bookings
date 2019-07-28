class Model():

    @classmethod
    def string(self,length):
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
    def primary(self):
        return 'PRIMARY KEY'
    
    @classmethod
    def not_null(self,val=True):
        return 'NOT NULL' if val else 'NULL'

    @classmethod
    def foreignkey(self,ref,on_delete_cascade=True):
        cascade = 'ON DELETE CASCADE' if on_delete_cascade else ''
        table,column = ref.split('.')
        return ',FOREIGN KEY (user_id) REFERENCES {}({}) {}'.format(table,column,cascade)

    @classmethod
    def create(cls):
        string = '''CREATE TABLE {} ({})'''.format(cls.__name__.lower(),','.join([i for i in cls.parse_fields().values()]))
        
        return string
    
    @classmethod
    def parse_fields(cls):
        dict1 = {key: key+' '+' '.join(value) for (key,value) in cls.__dict__.items() if key[:1]!='_'}
        return dict1
    
    @classmethod
    def fields(cls,*args,**kwargs):
        return args

    ## create save method
    ## update method
    ## get by id
    ## get by kwargs
    ## delete
    ## join method