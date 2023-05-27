const remote_host = "http://127.0.0.1:5000/";

export const getter = (resource, process/*, setLoading, setErr*/) => {
    const target = remote_host + resource;
    console.log("Starting GET request from ", target);
    fetch(target)
        .then((resp) => {
            if (!resp.ok) {
                throw new Error("Status code from getting " + target + ": " + resp.status);
            }

            return resp.json();
        })
        .then((json) => {
            console.log("Response to GET from " + target + ": " + json);
            process(json);
        })
        .catch((err) => {
            console.log(err);
        })
};

