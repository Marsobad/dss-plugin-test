// Access the parameters that end-users filled in using webapp config
// For example, for a parameter called "input_dataset"
// input_dataset = dataiku.getWebAppConfig()['input_dataset']


function modifyText(event) {
  console.log(document.getElementById("parameter-name").value);
  let headers = new Headers();
  let init = {
        method : 'GET',
        headers : headers};
  let url = getWebAppBackendUrl('/post_parameter');
  
  event.preventDefault();
}

const el = document.getElementById("Submit");
el.addEventListener("click", function (event) {modifyText(event)}, false);
