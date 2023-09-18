# Coffee Shop 

Small conversational AI for an imaginary coffee shop. Check the [challenge description](./CHALLENGE.md) for further details.

## Requirements

- Python (~3.10) 🐍
- Poetry
- Pytest

## Executing

1. Install the dependencies:

    ```
    cd coffeeshop/
    poetry install
    ```

2. Split the terminal into two to run Guest and Application:

    Server
    ```sh
    make run-server
    ```
    
    Guest
    ```sh
    make run-client $(FILEPATH)
    ```

There is a test file at `./data/sentences.txt`:

    ```sh
    make run-client FILEPATH=./data/sentences.txt
    ```

### Testing

```sh
make test
```

```sh
make coverage
```