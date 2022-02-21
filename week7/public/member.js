function get_name() {
  const search_name = document.getElementById("input_field").value
  const url = `http://127.0.0.1:3000/api/members?username=${search_name}`

  fetch(url)
    .then((res) => {
      return res.json()
    })
    .then((data) => {
      // console.log(data)
      const div_result = document.getElementById('result')
      if (data.data) {
        const username = data.data.username
        const name = data.data.name
        div_result.textContent = `${username} (${name})`

      } else {
        div_result.textContent = "無此會員"
      }
    })
    .catch(err => console.log("error"))

}
