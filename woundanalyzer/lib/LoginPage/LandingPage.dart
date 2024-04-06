import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:woundanalyzer/LoginPage/Loginpage.dart';
import 'package:woundanalyzer/LoginPage/Signuppage.dart';
import 'package:woundanalyzer/const.dart';

class LandingPage extends StatefulWidget {
  const LandingPage({super.key});

  @override
  State<LandingPage> createState() => _LandingPageState();
}

class _LandingPageState extends State<LandingPage> {
  late Color myColor;
  late Size mediaSize;

  @override
  Widget build(BuildContext context) {
    myColor = Theme.of(context).primaryColor;
    mediaSize = MediaQuery.of(context).size;
    return Container(
      color: Colors.white,
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: Stack(children: [
          Positioned(top: 80, child: _buildTop()),
          Positioned(bottom: 0, child: _buildBottom()),
        ]),
      ),
    );
  }

  Widget _buildTop() {
    return SizedBox(
      width: mediaSize.width,
      child: Column(mainAxisSize: MainAxisSize.min, children: [
        Material(
            borderRadius: BorderRadius.circular(25),
            // elevation: 10,
            child: Container(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(25),
                color: Colors.white,
              ),
              child: Padding(
                padding: const EdgeInsets.all(8.0),
                child: Column(
                  children: [
                    Image.asset(
                      "lib/assets/landing_illustration.png",
                      // height: 180,
                      // width: 200,
                    ),
                    // Row(
                    //   mainAxisAlignment: MainAxisAlignment.center,
                    //   children: [
                    //     Text(
                    //       "WoundAnalyzer",
                    //       style: TextStyle(
                    //           fontSize: 22, fontWeight: FontWeight.bold),
                    //     ),
                    //     Icon(
                    //       CupertinoIcons.search,
                    //       size: 22,
                    //     ),
                    //   ],
                    // ),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(
                          CupertinoIcons.search,
                          color: Colors.grey.shade600,
                          size: 22,
                        ),
                        SizedBox(
                          width: 2,
                        ),
                        AnimatedTextKit(
                          repeatForever: true,
                          animatedTexts: [
                            TypewriterAnimatedText(
                              "WoundAnalyzer",
                              //speed: Duration(seconds: 1),
                              textStyle: TextStyle(
                                  fontSize: 22.0,
                                  fontWeight: FontWeight.w900,
                                  color: Colors.grey.shade600),
                            )
                          ],
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            )),
      ]),
    );
  }

  Widget _buildBottom() {
    return Container(
      color: Colors.white,
      height: mediaSize.height / 2,
      width: mediaSize.width,
      child: Card(
        color: Colors.white,
        shape: const RoundedRectangleBorder(
            borderRadius: BorderRadius.only(
          topLeft: Radius.circular(30),
          topRight: Radius.circular(30),
        )),
        child: Padding(
          padding: const EdgeInsets.all(32.0),
          child: _buildForm(),
        ),
      ),
    );
  }

  Widget _buildForm() {
    return Column(mainAxisAlignment: MainAxisAlignment.center, children: [
      Container(
        color: Color(kbgwhite),
        padding: EdgeInsets.fromLTRB(18, 5, 18, 5),
        width: double.infinity,
        child: ElevatedButton(
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => SignupPage()),
            );
          },
          child: Text(
            'Sign up',
            style: TextStyle(
              fontWeight: FontWeight.w600,
              color: Colors.white,
              fontSize: 20.0,
            ),
          ),
          style: ElevatedButton.styleFrom(
            backgroundColor: Color(kbluepastle),
            elevation: 3,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(10.0),
            ),
            padding: EdgeInsets.symmetric(horizontal: 20.0, vertical: 20.0),
          ),
        ),
      ),
      Container(
        padding: EdgeInsets.fromLTRB(18, 5, 18, 5),
        width: double.infinity,
        child: OutlinedButton(
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => LoginPage()),
            );
          },
          child: Text(
            'Log in',
            style: TextStyle(
                color: Color(kbluepastle),
                fontWeight: FontWeight.bold,
                fontSize: 20.0),
          ),
          style: OutlinedButton.styleFrom(
            side: BorderSide(
                color: Color(kbluepastle),
                width: 1), // Set border color and width
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(10), // Set border radius
            ),
            padding: EdgeInsets.symmetric(horizontal: 20.0, vertical: 20.0),
          ),
        ),
      ),
    ]);
  }
}
