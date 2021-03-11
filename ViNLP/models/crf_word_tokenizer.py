import shutil

import sklearn_crfsuite


class CRFTokenizer(sklearn_crfsuite.CRF):
    def save(self, model_filename):
        destination = model_filename
        source = self.modelfile.name
        shutil.copy(src=source, dst=destination)  # type: ignore

    @staticmethod
    def load(model_filename):
        model = CRFTokenizer(model_filename=model_filename)
        return model
