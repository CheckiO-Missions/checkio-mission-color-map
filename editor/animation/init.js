//Dont change it
requirejs(['ext_editor_1', 'jquery_190', 'raphael_210', 'snap.svg_030'],
    function (ext, $, Raphael, Snap) {

        var cur_slide = {};

        ext.set_start_game(function (this_e) {
        });

        ext.set_process_in(function (this_e, data) {
            cur_slide = {};
            cur_slide["in"] = data[0];
            this_e.addAnimationSlide(cur_slide);
        });

        ext.set_process_out(function (this_e, data) {
            cur_slide["out"] = data[0];
        });

        ext.set_process_ext(function (this_e, data) {
            cur_slide.ext = data;
        });

        ext.set_process_err(function (this_e, data) {
            cur_slide['error'] = data[0];
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_animate_success_slide(function (this_e, options) {
            var $h = $(this_e.setHtmlSlide('<div class="animation-success"><div></div></div>'));
            this_e.setAnimationHeight(115);
        });

        ext.set_animate_slide(function (this_e, data, options) {
            var $content = $(this_e.setHtmlSlide(ext.get_template('animation'))).find('.animation-content');
            if (!data) {
                console.log("data is undefined");
                return false;
            }

            //YOUR FUNCTION NAME
            var fname = 'color_map';

            var checkioInput = data.in || [
                [0, 0, 0],
                [0, 1, 1],
                [0, 0, 2]
            ];
            var checkioInputStr = fname + '(' + JSON.stringify(checkioInput).replace(
                /\[/g, "(").replace(/]/g, ")").replace("))", "),)").replace(/\),/g, ",),") + ')';

            var failError = function (dError) {
                $content.find('.call').html(checkioInputStr);
                $content.find('.output').html(dError.replace(/\n/g, ","));

                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
                $content.find('.answer').remove();
                $content.find('.explanation').remove();
                this_e.setAnimationHeight($content.height() + 60);
            };

            if (data.error) {
                failError(data.error);
                return false;
            }

            if (data.ext && data.ext.inspector_fail) {
                failError(data.ext.inspector_result_addon);
                return false;
            }

            $content.find('.call').html(checkioInputStr);
            $content.find('.output').html('Working...');

            var svg = new SVG($content.find(".explanation")[0]);
            svg.draw(checkioInput);


            if (data.ext) {
                var rightResult = data.ext["answer"];
                var userResult = data.out;
                var result = data.ext["result"];
                var result_addon = data.ext["result_addon"];

                svg.color(userResult);

                //if you need additional info from tests (if exists)
                var explanation = data.ext["explanation"];
                $content.find('.output').html('&nbsp;Your result:&nbsp;' + JSON.stringify(userResult));
                if (!result) {
                    $content.find('.answer').html(result_addon);
                    $content.find('.answer').addClass('error');
                    $content.find('.output').addClass('error');
                    $content.find('.call').addClass('error');
                }
                else {
                    $content.find('.answer').remove();
                }
            }
            else {
                $content.find('.answer').remove();
            }


            //Your code here about test explanation animation
            //$content.find(".explanation").html("Something text for example");
            //
            //
            //
            //
            //


            this_e.setAnimationHeight($content.height() + 60);

        });

        //This is for Tryit (but not necessary)
//        var $tryit;
//        ext.set_console_process_ret(function (this_e, ret) {
//            $tryit.find(".checkio-result").html("Result<br>" + ret);
//        });
//
//        ext.set_generate_animation_panel(function (this_e) {
//            $tryit = $(this_e.setHtmlTryIt(ext.get_template('tryit'))).find('.tryit-content');
//            $tryit.find('.bn-check').click(function (e) {
//                e.preventDefault();
//                this_e.sendToConsoleCheckiO("something");
//            });
//        });


        function SVG(dom) {

            var colorOrange4 = "#F0801A";
            var colorOrange3 = "#FA8F00";
            var colorOrange2 = "#FAA600";
            var colorOrange1 = "#FABA00";

            var colorBlue4 = "#294270";
            var colorBlue3 = "#006CA9";
            var colorBlue2 = "#65A1CF";
            var colorBlue1 = "#8FC7ED";

            var colorGrey4 = "#737370";
            var colorGrey3 = "#9D9E9E";
            var colorGrey2 = "#C5C6C6";
            var colorGrey1 = "#EBEDED";

            var colorWhite = "#FFFFFF";

            var paper;

            var padding = 10;

            var cell = 30;

            var fourColors = [colorGrey3, colorBlue2, colorOrange1, colorOrange3];

            var aCell = {"fill": colorGrey1, "stroke": colorBlue4, "stroke-width": 2};
            var aNumb = {"stroke": colorBlue4, "font-family": "Roboto, Arial, sans", "font-size": cell * 0.5};

            var grid;

            this.draw = function (matrix) {
                paper = Raphael(dom, cell * matrix[0].length + 2 * padding,
                    cell * matrix.length + 2 * padding);
                grid = paper.set();
                for (var i = 0; i < matrix.length; i++) {
                    var row = paper.set();
                    for (var j = 0; j < matrix[0].length; j++) {
                        var r = paper.rect(padding + cell * j, padding + cell * i, cell,
                            cell).attr(aCell);
                        r.mark = matrix[i][j];
                        row.push(r);
                        paper.text(padding + cell * (j + 0.5), padding + cell * (i + 0.5),
                            matrix[i][j]).attr(aNumb);
                    }
                    grid.push(row);
                }
            };

            this.color = function(colorArray) {
                if (!Array.isArray(colorArray)) {
                    return false;
                }
                for (var i = 0; i < grid.length; i++) {
                    for (var j = 0; j < grid[i].length; j++) {
                        var r = grid[i][j];
                        var color = colorArray[r.mark];
                        if (color && [1, 2, 3, 4].indexOf(color) !== -1) {
                            r.attr("fill", fourColors[color - 1]);
                        }
                    }
                }
            }

        }


    }
);
