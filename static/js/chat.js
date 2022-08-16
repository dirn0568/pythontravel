document.getElementById('chat_send').addEventListener('keydown', function(){
    if (window.event.keyCode == 13) {
        document.getElementById('chat_data_text').submit();
    }
    console.log("안돼냐?")
});


//const $drop = document.querySelector(".dropBox");
//
//// 드래그한 파일 객체가 해당 영역에 놓였을 때
//$drop.ondrop = (e) => {
//  e.preventDefault();
//
//  // 드롭된 파일 리스트 가져오기
//  //  console.dir(e.dataTransfer);
//  //  var data = e.dataTransfer.files[0]; // 파일 하나만 저장
//  //  console.dir(data);
//
//  const files = [...e.dataTransfer?.files]; // 파일 여러개 저장
//  console.log(files);
//  console.log(files[0]);
//  chat_test.innerHTML = files.map(v => v.name).join("<br>");
//  //.getElementById('chat_1').innerHTML = files.map(v => v.name).join("<br>");
//  //dragArea.classList.add('active');
//
//  //  formData.append('pic',document.getElementById('chat_1').files[0]);
//}
//
//// ondragover 이벤트가 없으면 onDrop 이벤트가 실핻되지 않습니다.
//$drop.ondragover = (e) => {
//  e.preventDefault();
//}
//
//// 드래그한 파일이 최초로 진입했을 때
//$drop.ondragenter = (e) => {
//  e.preventDefault();
//
//  $drop.classList.add("active");
//}
//
//// 드래그한 파일이 영역을 벗어났을 때
//$drop.ondragleave = (e) => {
//  e.preventDefault();
//
//  $drop.classList.remove("active");
//}



// 채팅창 마지막 보루
//$('input[type="file"]').on('change', function(e){
//  var fileName = e.target.files[0].name;
//  if (fileName) {
//    $(e.target).parent().attr('data-message', fileName);
//  }
//  console.log('두두등장 두두등장');
//});
//
//  $(document).on('drag dragstart dragend dragover dragenter dragleave drop', function(e) {
//    console.log("실행중이냐공요요요요요?")
//    if ($('input[type="file"]').length) {
//      if (['dragover', 'dragenter'].indexOf(e.type) > -1) {
//        if (window.dragTimeout)
//          clearTimeout(window.dragTimeout);
//        $('body').addClass('dragged');
//      } else if (['dragleave', 'drop'].indexOf(e.type) > -1) {
//        // Without the timeout, some dragleave events are triggered
//        // when the :after appears, making it blink...
//        window.dragTimeout = setTimeout(function() {
//          $('body').removeClass('dragged');
//        }, 100);
//      }
//    }
//    $('input[type="file"]').on('change', function(e){
//      var fileName = e.target.files[0].name;
//      if (fileName) {
//        $(e.target).parent().attr('data-message', fileName);
//      }
//      console.log('두두등장 두두등장');
//    });
//  });

 $('input[type="file"]').on('change', function(e){
    var fileName = e.target.files[0].name;
    if (fileName) {
      $(e.target).parent().attr('data-message', fileName);
      if (!confirm("정말로 파일을 전송하시겠습니까?")) {
          alert("취소 되었습니다.");
      } else {
          document.getElementById('chat_data_file').submit();
      }
    }
  });

  $(document).on('drag dragstart dragend dragover dragenter dragleave drop', function(e) {
    if ($('input[type="file"]').length) {
      if (['dragover', 'dragenter'].indexOf(e.type) > -1) {
        if (window.dragTimeout)
          clearTimeout(window.dragTimeout);
        $('body').addClass('dragged');
      } else if (['dragleave', 'drop'].indexOf(e.type) > -1) {
        // Without the timeout, some dragleave events are triggered
        // when the :after appears, making it blink...
        window.dragTimeout = setTimeout(function() {
          $('body').removeClass('dragged');
        }, 100);
      }
    }
  });