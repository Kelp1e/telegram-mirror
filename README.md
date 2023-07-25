# Telethon Bot: Your Channel Aggregator

This **Python** script, powered by **Telethon**, allows you to aggregate messages from all the groups you are subscribed to into a single channel. It serves as a convenient channel aggregator, bringing all the important messages together in one place.

## Features

- **Message Aggregation**: Automatically collects messages from multiple groups and channels into a centralized channel.
- **Effortless Setup**: Simply set up your Telethon API credentials.
- **Easy Deployment**: Deploy the bot on any compatible server or cloud platform.

## Getting Started

To get started with the **Telethon Bot**, you have two options: running it directly on your machine or using **Docker**.

### Running on Your Machine
1. Clone this repository to your local machine `git clone https://github.com/Kelp1e/telegram-mirror.git`
2. Create an `.env` file based on the `.env.example` file and configure it.
3. Create and activate a virtual environment `python -m venv venv ; venv/Scripts/activate`
4. Install the required dependencies by running `pip install -r requirements.txt`
5. Run the script using `python main.py` and start aggregating messages.

### Running with Docker
1. Make sure you have **Docker** installed on your machine. If not, you can download it from the [Docker](https://www.docker.com/) and follow the installation instructions specific to your operating system.
2. Clone this repository to your local machine `git clone https://github.com/Kelp1e/telegram-mirror.git`
3. Create an `.env` file based on the `.env.example` file and configure it.
4. Build the **Docker** image `docker build -t telegram-mirror .`
5. After the image is built successfully, run the **Telethon Bot** inside a **Docker** container `docker run -it telegram-mirror`


## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.
