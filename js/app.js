/**
 * Created by flame on 2017/6/13.
 */
function NoteCtrl($scope) {
    //
    $scope.content= "";
    $scope.getRestCount= function(){
        return 100 - $scope.content.length;
    }
    // 保存的方法
    $scope.save = function () {
        //保存数据
        sessionStorage.setItem('note_key',$scope.content);
        // 清空用户输入
        $scope.content= "";
        // 提示
        alert("保存成功");
    }
    //清空的方法
    $scope.clear = function () {
        //
        $scope.content = '';
        alert('清除成功');
    };

    // 读取的方法
    $scope.read = function () {
        var item = sessionStorage.getItem('note_key');
        if (item){
            $scope.content = item;
            alert('数据读取成功');
        }else {
            alert('还没有保存数据');
        }

    };
}