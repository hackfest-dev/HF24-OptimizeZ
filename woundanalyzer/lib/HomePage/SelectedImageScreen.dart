import 'dart:io';

import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:scanning_effect/scanning_effect.dart';
import 'package:woundanalyzer/const.dart';

class SelectedImageScreen extends StatefulWidget {
  final String imagePath;

  const SelectedImageScreen({Key? key, required this.imagePath})
      : super(key: key);

  @override
  State<SelectedImageScreen> createState() => _SelectedImageScreenState();
}

class _SelectedImageScreenState extends State<SelectedImageScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          iconTheme: IconThemeData(color: Colors.white),
          backgroundColor: Color(kbluepastle),
          title: Text(
            'Selected Image',
            style: TextStyle(color: Colors.white),
          ),
        ),
        body: Container(
          width: double.infinity,
          child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Container(
                  height: 320,
                  width: 320,
                  child: ScanningEffect(
                    scanningColor: Color(kbluepastle),
                    borderLineColor: Colors.blue,
                    delay: Duration(seconds: 1),
                    duration: Duration(seconds: 2),
                    child: Container(
                      child: Image.file(
                        File(widget.imagePath),
                        fit: BoxFit.cover,
                      ),
                    ),
                  ),
                ),
                DefaultTextStyle(
                  style: const TextStyle(
                    fontSize: 32.0,
                    fontWeight: FontWeight.bold,
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: SizedBox(
                      height: 35,
                      width: double.infinity,
                      child: Center(
                        child: AnimatedTextKit(
                          animatedTexts: [
                            FadeAnimatedText("Analyzing Wound..",
                                textStyle: TextStyle(
                                    color: Color(kbluepastle), fontSize: 20)),
                          ],
                          onTap: () {
                            print("Tap Event");
                          },
                        ),
                      ),
                    ),
                  ),
                ),
              ]),
        ));
  }
}
