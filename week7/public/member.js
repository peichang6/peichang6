function get_name() {
  const search_name = document.getElementById("input_field").value
  const url = `http://127.0.0.1:3000/api/members?username=${search_name}`

  fetch(url)
    .then((res) => {
      return res.json()
    })
    .then((data) => {
      // console.log(data)
      const div = document.createElement("div")
      div.classList.add("results")
      if (data.data) {
        const username = data.data.username
        const name = data.data.name
        div.textContent = `${username} (${name})`
        document.getElementsByClassName("result")[0].appendChild(div)
      } else {
        div.textContent = "無此會員"
        document.getElementsByClassName("result")[0].appendChild(div)
      }
    })
    .catch(err => console.log("error"))

}