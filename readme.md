# NewsCat Classifier

NewsCat Classifier is a Python-based project for extracting news articles from provided URLs, storing them in a database, and classifying them into categories such as protest, terrorism, natural-disaster, politics, positive, and others using NLP techniques and TensorFlow with SpaCy.

## Getting Started

These instructions will guide you through setting up and running the project on your local machine.

### Prerequisites

- Python 3.x
- PostgreSQL
- Redis
- Git

### Installation

1. Clone the repository:
    ```bash
    git clone [URL_to_this_repository]
    ```

2. Navigate to the cloned directory:
    ```bash
    cd [cloned_directory]
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

- Initialize the PostgreSQL database and update the database URLs in the `models/settings.py` file.

### Redis Setup

- Install and initialize Redis on Windows using WSL:
    ```bash
    sudo apt update
    sudo apt install redis-server
    sudo service redis-server start
    ```

### Data Models

- Pre-trained classification models are stored in the `data_models` directory.
    - Example: `data_models\model_020_93_065_83_nl.h5`
        - Training Loss: 0.20
        - Training Accuracy: 0.93
        - Validation Loss: 0.65
        - Validation Accuracy: 0.83

### Celery Setup

- Initialize Celery (ensure Redis is running as the broker):
   - On Windows:
     ```bash
     celery -A your-application worker -l info --pool=solo
     ```
   - On Linux:
     ```bash
     celery -A your-application worker -l info
     ```

### Running the Application

1. Update the `celery_fun.py` file as needed for your Celery configuration.

2. To start the application, run:
    ```bash
    python main.py
    ```
   - The links for news articles to be processed are specified in `main.py`.

## Built With

- [Python](https://www.python.org/) - The programming language used.
- [TensorFlow](https://www.tensorflow.org/) and [SpaCy](https://spacy.io/) - For NLP and classification tasks.
- [PostgreSQL](https://www.postgresql.org/) - The database used.
- [Redis](https://redis.io/) - Used for managing Celery task queue.
- [Celery](https://docs.celeryproject.org/en/stable/) - Distributed task queue.


