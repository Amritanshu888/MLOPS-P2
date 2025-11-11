from dataclasses import dataclass ## This acts like a decorator which probably creates variable for an empty class
## Suppose u have a class where u don't have functions defined , u want to define a certain set of variables

## The output of data ingestion we will call it as data ingestion artifact
@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
