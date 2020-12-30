// Access the parameters that end-users filled in using webapp config
// For example, for a parameter called "input_dataset"
// input_dataset = dataiku.getWebAppConfig()['input_dataset']

function modifyText(event) {
  let formData = new FormData(document.getElementById('form-sample'));
  let data = new URLSearchParams(formData);
  let headers = new Headers();
  let init = {
        method : 'POST',
        headers : headers,
        body: data};

  let url = getWebAppBackendUrl('/post_parameter');
  let promise = fetch(url, init) 
  .then(function(response){ 
      console.log(response);
  });
  event.preventDefault();
}

const el = document.getElementById("Submit");
el.addEventListener("click", function (event) {modifyText(event)}, false);
