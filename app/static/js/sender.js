async function sender(url, data, method = 'post') {
    var m_url = location.hostname

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(data);

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
    };
    let response = await fetch(url, requestOptions);
    if (response.ok) { // если HTTP-статус в диапазоне 200-299
        json = await response.json();
        return (json)

    } else {
        console.log("Ошибка HTTP: " + response.status);
    }

};