from deprecated import deprecated

from Index.BaseIndex import BaseIndex


@deprecated
class MetaDataIndex(BaseIndex):
    _instances = {}

    def __new__(cls, config, name, data_dir, index_dir):
        if name not in cls._instances:
            instance = super(MetaDataIndex, cls).__new__(cls)
            cls._instances[name] = instance
        return cls._instances[name]

    def __init__(self, config, name, data_dir, index_dir):
        super().__init__(config, name, data_dir, index_dir)
        self.name = name

    def _update_index(self):
        pass
        # transformations = [SentenceSplitter(), self.embed_model]
        # pipeline = IngestionPipeline(
        #     transformations=transformations,
        # )
        # reader = SimpleDirectoryReader(input_dir=self.data_dir)
        # documents = reader.load_data()
        # nodes = pipeline.run(documents=documents)
        # self.index = VectorStoreIndex(
        #     nodes=nodes,
        #     embed_model=self.embed_model,
        # )
        # reader = SimpleDirectoryReader(input_dir=self.data_dir)
        # documents = reader.load_data()
        # self.index = VectorStoreIndex(documents,insert_batch_size=1024)

    def _get_retrieve_top_k(self):
        return self.config.metadata_retrieve_top_k
