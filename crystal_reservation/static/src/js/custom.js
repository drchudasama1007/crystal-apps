var cfg = {
  tables: [
    {
      id: "A",
      seats: [1, 2, 3, 4, 5, 6, 7, 8],
      x: 10,
      y: 34
    },
    {
      id: "B",
      seats: [1, 2, 3, 4, 5],
      x: 25,
      y: 15
    },
    {
      id: "C",
      seats: [1, 2, 3, 4, 5, 6, 7, 8],
      x: 40,
      y: 15
    },
    {
      id: "D",
      seats: [1, 2, 3, 4, 5, 6, 7, 8],
      x: 55,
      y: 15
    },
    {
      id: "E",
      seats: [1, 2, 3, 4, 5, 6, 7, 8],
      x: 70,
      y: 15
    },
    {
      id: "F",
      seats: [1, 2, 3, 4, 5, 6, 7, 8],
      x: 85,
      y: 34
    },
    {
      id: "G",
      seats: [1, 2, 3, 4, 5, 6, 7, 8],
      x: 70,
      y: 65
    },
    {
      id: "H",
      seats: [1, 2, 3, 4, 5, 6, 7, 8],
      x: 55,
      y: 65
    },
    {
      id: "I",
      seats: [1, 2, 3, 4, 5, 6, 7, 8],
      x: 40,
      y: 65
    },
    {
      id: "J",
      seats: [1, 2, 3, 4, 5, 6, 7, 8],
      x: 25,
      y: 65
    }
  ],
  rsvp: {
    A2: "Tim",
    A3: "Sheena",
    C1: "John",
    D4: "Anita"
  }
};

initboard();

//rerender tables
function initboard() {
  $.each(cfg.tables, function (index, t) {
    //Add table container
    $("#tables").append(
      '<div class="table" data-table-id="' + t.id + '"></div>'
    );
    var table = $('[data-table-id="' + t.id + '"]');

    //Adjust position
    $('[data-table-id="' + t.id + '"]').css({
      left: t.x + "%",
      top: t.y + "%"
    });
    var tw = table.width(),
      th = table.height(),
      radius = tw - tw / 3,
      angle = 0,
      step = (2 * Math.PI) / t.seats.length;
    //Build seating
    $.each(t.seats, function (sid, s) {
      var seatid = t.id + sid,
        rsvp = cfg.rsvp[seatid] ? "reserved" : "";
      table.append(
        '<div class="seat ' +
          rsvp +
          '" data-seat-id="' +
          seatid +
          '" data-seat-id="' +
          s +
          '">' +
          seatid +
          "</div>"
      );
      var seat = $('[data-seat-id="' + seatid + '"]');

      var x = Math.round(tw / 2 + radius * Math.cos(angle) - seat.width() / 2),
        y = Math.round(th / 2 + radius * Math.sin(angle) - seat.height() / 2);
      seat.css({ left: x + "px", top: y + "px" });
      angle = angle + step;
    });
  });
}

//Table selection
$(document).on("click", ".table", function () {
  console.log($(this).hasClass("animated"));
  $(this).addClass("animated bounce");
  console.log("BOUNCE!");
});
