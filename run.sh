docker build -t covidnyc .
docker kill covid-nyc

echo "--- Sleeping for 2 Seconds .. why not?---"
sleep 2

echo "--- Starting Visualization App ---"

docker run \
    --rm \
    --init \
    --name covid-nyc \
    -v ${PWD}:/opt/scripts \
    -i \
    -p 8080:8080 \
    covidnyc \
    /bin/bash -c "python3.8 server.py"