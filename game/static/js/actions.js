let UpdateAnts = function () {
    $(".ant-card").remove();
    $.get("api/ants",
        function (data, textStatus) {
            $.each(data["ants"], function (i, val) {
                $(".ant-holder").append(`
				<div class="ant-card">
                    <img src="${val[0]}" alt="Ant image">
                    <span>x${val[1]}</span>
                    <button type="button" class="buy">$ ${val[2]}</button>
                </div>`);
            });
        });
}
let UpdateItems = function () {
    $(".item-card").remove();
    $.get("api/items",
        function (data, textStatus) {
            $.each(data["items"], function (i, val) {
                $(".item-holder").append(`
				<tr class="item-card">
                    <td><img src="${val[0]}" alt="Item image"></td>
                    <td><span>${val[1]}</span></td>
                    <td><button type="button" class="sell">$ ${val[2]}</button></td>
                </tr>`);
            });
        });
}

let UpdateMoney = function () {
    $.get("api/money",
        function (data, textStatus) {
            $(".user-money").html("$ " + data["money"]);
            alert("Че мы получили: " + data);
        });
}

let UpdateChest = function () {
    $.get("api/chest",
        function (data, textStatus) {
            if ($.isEmptyObject(data)) {
                alert("Потом сделаю");
            } else {
                alert("Это тоже потом");
            }
            alert("Че мы получили: " + data);
        });
}

$('.fight-open').click(function () {
    alert("Босс файт ёпта");
    $(".boss-window").display = "block";
});

$('.fight-close').click(function () {
    alert("Слился");
    $(".boss-window").display = "none";
});

$('.fight').click(function () {
    alert("Тебя отпиздили");
    $.post("api/boss/fight",
        {
            ants: 52,
        },
        function (data, textStatus) {
            alert("Че мы получили: " + data);
        });
    UpdateAnts();
});

$('.buy').click(function () {
    alert("Купить: " + parseInt($(this).text().substring(2)));
    $.get("api/ant/buy",
        function (data, textStatus) {
            $(this).html("$ " + data["cost"]);
            $("#total-ants").html("Всего: " + data["total"])
            alert("Че мы получили: " + data);
        });
    UpdateAnts();
    UpdateMoney();
});

$('.send-all').click(function () {
    $.post("api/ant/sendall",
        {},
        function (data, textStatus) {
            alert("Че мы получили: " + data);
        });
    UpdateAnts();
});

$('.sell').click(function () {
    $.post("api/item/sell",
        {
            name: parseInt($(this).prev().text())
        },
        function (data, textStatus) {
            alert("Че мы получили: " + data);
        });
    UpdateItems();
    UpdateMoney();
});

$('.sell-all').click(function () {
    $.post("api/item/sellall",
        {},
        function (data, textStatus) {
            alert("Че мы получили: " + data);
        });
	UpdateItems();
    UpdateMoney();
});

$('.chest-open').click(function () {
    $.post("api/chest/open",
        {},
        function (data, textStatus) {
            alert("Че мы получили: " + data);
        });
    UpdateChest();
});

$('.chest-sell').click(function () {
    $.post("api/chest/cell",
        {},
        function (data, textStatus) {
            alert("Че мы получили: " + data);
        });
    UpdateChest();
    UpdateMoney();
});