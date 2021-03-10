import shutil

import sklearn_crfsuite


class CRF(sklearn_crfsuite.CRF):
    def save(self, model_filename):
        destination = model_filename
        source = self.modelfile.name
        shutil.copy(src=source, dst=destination)

    @staticmethod
    def load(model_filename):
        model = CRF(model_filename=model_filename)
        return model
