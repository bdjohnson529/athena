# PDF Informational Retrieval

This project enables information retrieval from PDF document libraries.

## Setup
Instructions are provided for the Anaconda Prompt. Commands should be run from the base directory of the repository.

Install the Anaconda environment:
```
conda env create -f environment.yml
```

Run the application:
```
conda activate athena
set FLASK_APP=athena
set FLASK_ENV=development
flask init-db
flask run
```

To run on a specific port:
```
flask run -h localhost -p 3000
```


## Technical Roadmap
1. Convert the PDF to a JSON file.
2. Tokenize each page of the PDF.
3. Construct an inverted index of the document dictionary.


## Usage

### Part 1 - Converting PDFs to Text
Execute the following commands from the root of the repository, in the Anaconda prompt.

1. Create a `Data` folder in this repository, and load the PDFs into that folder.
Create a `data` folder which contains the MOR pdfs. The repository structure should resemble:
```
├── data
|	├── file_1.pdf
|	├── file_2.pdf
├── extract.py
```
2. Execute the `extract.py` script. The script took approximately 4 minutes to convert a 36MB PDF into a 3MB txt file.
```
conda activate athena
python extract.py "data\file_1.pdf" --outfile "data\file_1.txt"
```

## Contributing
After installing new packages to the venv, save the requirements to `requirements.txt` so that your dependencies are added to the repository.
```
conda env export > environment.yml
```
