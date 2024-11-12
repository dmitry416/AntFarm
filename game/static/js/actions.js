const csrftoken = $("[name=csrfmiddlewaretoken]").val();

function UpdateAnts() {
    $(".ant-card").remove();
    $.get("api/userants",
        function (data, textStatus) {
            let total = 0;
            $.each(data, function (i, val) {
                total += val["count"];
                if (val["is_sent"]) {
                    $(".ant-holder").append(`
			    	<div class="ant-card">
                        <img src="static/${val["ant_image"]}" alt="Ant image">
                        <span>${val["ant_name"]}</span>
                        <span>x${val["count"]}</span>
                        <button type="button" class="buy" style="background: #CCCCCC">В пути</button>
                    </div>`);
                } else {
                    $(".ant-holder").append(`
    				<div class="ant-card">
                        <img src="static/${val["ant_image"]}" alt="Ant image">
                        <span>${val["ant_name"]}</span>
                        <span>x${val["count"]}</span>
                        <button type="button" class="buy" onclick="BuyAnt(\'${val['ant_name']}\')">$ ${val['cost']}</button>
                    </div>`);
                }

            });
            $("#total-ants").html("Всего: " + total);
        });
}

function UpdateItems() {
    $(".item-card").remove();
    $.get("api/useritems",
        function (data, textStatus) {
            $.each(data, function (i, val) {
                $(".item-holder").append(`
				<tr class="item-card">
                    <td><img src="static/${val["item_image"]}" alt="Item image"></td>
                    <td><span>${val["item_name"]}</span></td>
                    <td><span>${val["count"]} x $ ${val["item_cost"]}</span></td>
                    <td><button type="button" class="sell" onclick="SellItem(\'${val['item_name']}\')">$ ${val["count"] * val["item_cost"]}</button></td>
                </tr>`);
            });
        });
}

function UpdateMoney() {
    $.get("api/usermoney",
        function (data, textStatus) {
            $(".user-money").html("$ " + data["money"]);
        });
}

function UpdateLeaderboard() {
    $.get("api/leaderboard/",
        function (data, textStatus) {
            $.each(data, function (i, val) {
                $(".leaderboard").append(`
                    <tr class="place">
                        <td class="place-item">${i + 1}</td>
                        <td class="place-item">${val["ant_count"]}</td>
                        <td class="place-item">${val["name"]}</td>
                    </tr>`)
            });
        });
}

function UpdateChest() {
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

function BuyAnt(name) {
    $.post("api/buyant/",
        {
            csrfmiddlewaretoken: csrftoken,
            "name": name
        },
        function (data, textStatus) {
            if (data["success"]) {
                $(this).html("$ " + data["cost"]);
                UpdateAnts();
                UpdateMoney();
            }
            // $("#total-ants").html("Всего: " + data["total"])
        });
}

function SellItem(name) {
    $.post("api/sellitem/",
        {
            csrfmiddlewaretoken: csrftoken,
            "name": name
        },
        function (data, textStatus) {
            UpdateItems();
            UpdateMoney();
        });
}

function returnAnts() {
    $.get("api/getrewardtime/",
        function (data, textStatus) {
            if (data["onway"]) {
                $.post("api/getreward/",
                    {csrfmiddlewaretoken: csrftoken},
                    function (data, textStatus) {
                        UpdateItems();
                        UpdateAnts();
                    });
            }
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

$('.send-all').click(function () {
    $.post("api/sendall/",
        {csrfmiddlewaretoken: csrftoken},
        function (data, textStatus) {
            UpdateAnts();
        });

});

$('.sell-all').click(function () {
    $.post("api/sellall/",
        {csrfmiddlewaretoken: csrftoken},
        function (data, textStatus) {
            UpdateItems();
            UpdateMoney();
        });
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

let main = function () {
    UpdateItems();
    UpdateAnts();
    UpdateLeaderboard();
    UpdateMoney();
    setInterval(returnAnts, 5000);
}

main();