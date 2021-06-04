function validateForm() {
    let number = parseInt($("input[name='number']").val())
    let current = parseInt($("input[name='current_num']").val())
    if (number < 1 || number > 10 || current < 1 || current > number) {
        alert("掛號號碼之範圍為1~10號，目前號碼應在前")
        return false;
    }
}
$(".add-delay-time").on("click", function () {
    $(".delay-time-list").append(`
    <li>
      <h3>
        臨時緊急狀況<input type="text" class="situation" />，
        預估延遲<input type="number" class="delay-time" value="10" />分鐘
      </h3>
    </li>
    `)
})