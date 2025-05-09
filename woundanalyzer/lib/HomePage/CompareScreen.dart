import 'dart:async';

import 'dart:io';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;

class SelectImageScreen extends StatefulWidget {
  const SelectImageScreen({Key? key}) : super(key: key);

  @override
  State<SelectImageScreen> createState() => _SelectImageScreenState();
}

class _SelectImageScreenState extends State<SelectImageScreen> {
  String? imagePath;
  bool isLoading = false;
  Map<String, dynamic>? dummyResults;

  Future<void> uploadImage(String imageFile) async {
    try {
      var uri = Uri.parse('http://192.168.137.26:5000/post_img');
      var request = http.MultipartRequest('POST', uri);

      request.files.add(await http.MultipartFile.fromPath('file', imageFile));

      var response = await request.send();
      if (response.statusCode == 200) {
        print('Image uploaded successfully');
        // Simulate API response
        setDummyResults({
          "severity": "Moderate",
          "comparison": {
            "message": "Improvement noticed",
            "prev_severity": "Severe",
            "curr_severity": "Moderate"
          },
          "healing_rate": "10% per week"
        });
      } else {
        print('Failed to upload image. Status code: ${response.statusCode}');
      }
    } catch (e) {
      print('Error uploading image: $e');
    }
  }

  Future<void> _pickImage(BuildContext context, ImageSource source) async {
    final ImagePicker _picker = ImagePicker();
    final XFile? image = await _picker.pickImage(source: source);
    if (image != null) {
      setState(() {
        imagePath = image.path;
      });
      // Simulate image upload
      await uploadImage(image.path);
    }
  }

  void setDummyResults(Map<String, dynamic> results) {
    setState(() {
      dummyResults = results;
    });
  }

  Future<void> _showCompareLoader() async {
    setState(() {
      isLoading = true;
    });

    // Simulate a delay of 3 seconds
    await Future.delayed(const Duration(seconds: 3));

    // Set dummy results after delay
    setDummyResults({
      "severity": "Moderate",
      "comparison": {
        "message": "Improvement noticed",
        "prev_severity": "Severe",
        "curr_severity": "Moderate"
      },
      "healing_rate": "10% per week"
    });

    setState(() {
      isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Select Image')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            if (imagePath != null)
              Image.file(
                File(imagePath!),
                height: 200,
                width: 200,
                fit: BoxFit.cover,
              )
            else
              const Icon(
                Icons.image,
                size: 200,
                color: Colors.grey,
              ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: () {
                showModalBottomSheet(
                  context: context,
                  builder: (BuildContext context) {
                    return Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        ListTile(
                          leading: const Icon(Icons.photo_library),
                          title: const Text('Open Gallery'),
                          onTap: () {
                            Navigator.pop(context);
                            _pickImage(context, ImageSource.gallery);
                          },
                        ),
                        ListTile(
                          leading: const Icon(Icons.camera_alt),
                          title: const Text('Open Camera'),
                          onTap: () {
                            Navigator.pop(context);
                            _pickImage(context, ImageSource.camera);
                          },
                        ),
                      ],
                    );
                  },
                );
              },
              child: const Text('Select Image'),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed:
                  imagePath != null && !isLoading ? _showCompareLoader : null,
              child: const Text('Compare'),
            ),
            const SizedBox(height: 16),
            if (isLoading)
              const CircularProgressIndicator()
            else if (dummyResults != null)
              Padding(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text("Severity: ${dummyResults!['severity']}"),
                    Text(
                        "Comparison: ${dummyResults!['comparison']['message']}"),
                    Text(
                        "Previous Severity: ${dummyResults!['comparison']['prev_severity']}"),
                    Text(
                        "Current Severity: ${dummyResults!['comparison']['curr_severity']}"),
                    Text("Healing Rate: ${dummyResults!['healing_rate']}"),
                  ],
                ),
              ),
          ],
        ),
      ),
    );
  }
}
