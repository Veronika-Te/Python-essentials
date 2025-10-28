from typing import List

class AIModel:
  framework= "TensorFlow"
  def __init__(self,model_name: str, accuracy: float):
    self.model_name=model_name
    self.accuracy=accuracy
  
  def display_info(self):
    print(f"Framework: {AIModel.framework}, Name: {self.model_name}, Accuracy: {self.accuracy}")

class DataPreprocessor:
  def __init__(self, method: str, feature_count: int):
    self.method=method
    self.feature_count=feature_count
    
  def __str__(self):
    return f"Preprocessor using {self.method} on {self.feature_count} features"

class AIPipeline:
  pipeline_count=0
  
  def __init__(self, name: str, steps: List[str]):
    self.name=name
    self.steps=steps
    AIPipeline.pipeline_count+=1
    
  def __str__(self):
    steps_str = ", ".join(self.steps)
    return f"Pipeline name: {self.name}, Steps: {self.steps}"
  
class ModelEvaluator:
  def __init__(self, model_name: str, metrics: List[str] = ["accuracy"]):
    self.model_name=model_name
    self.metrics=metrics
    
  def evaluate(self):
    metrics_str = ", ".join(self.metrics)
    return f"Evaluating {self.model_name} using {metrics_str}"

class AIDataset:
  data_format="CSV"
  def __init__(self, dataset_name: str, sample_count:int):
    self.dataset_name=dataset_name
    self.sample_count=sample_count
    
  def __str__(self):
    return f"Dataset: {self.dataset_name}, Samples: {self.sample_count}, Format: {AIDataset.data_format}"

def main():
  ai_model1=AIModel("ImageClassifier",95.2)
  ai_model1.display_info()
  dp1=DataPreprocessor("Normalization", 20)
  print(dp1)

  pipeline1 = AIPipeline("Main Pipeline", ["cleaning", "training", "evaluation"])
  print(pipeline1)
  print(f"Total pipelines created: {AIPipeline.pipeline_count}")

  evaluator1 = ModelEvaluator("ImageClassifier")
  print(evaluator1.evaluate())

  dataset1 = AIDataset("Titanic", 891)
  print(dataset1)

if __name__=="__main__":
  main()