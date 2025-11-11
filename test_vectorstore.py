from vectorstore import VectorStore


def test_add_and_search():
vs = VectorStore(dim=384)
docs = [{'id':'1','text':'wheat is a cereal crop','source':'x'},{'id':'2','text':'rice requires standing water','source':'y'}]
vs.add_documents(docs)
res = vs.similarity_search('how to grow rice', k=1)
assert len(res) == 1
