import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/material.dart';
import 'package:woundanalyzer/HomePage/AccountDetailspage.dart';
import 'package:woundanalyzer/HomePage/Components/Appbar.dart';
import 'package:woundanalyzer/HomePage/Components/Bottomnavabar.dart';
import 'package:woundanalyzer/const.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _selectedIndex = 0; // Define selectedIndex here

  final List<Widget> _screens = [HomeScreen(), AccountDetailsPage()];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index; // Update _selectedIndex when tab is tapped
    });
  }

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        body: _screens[selectedIndex],
        bottomNavigationBar: BottomNavBar(),
      ),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: CustomScrollView(
        slivers: [
          const SliverPersistentHeader(
            delegate: SliverSearchAppBar(),
            pinned: true,
          ),
          SliverList(
              delegate:
                  SliverChildBuilderDelegate((BuildContext context, int index) {
            return Container(
                margin: const EdgeInsets.all(8),
                padding: const EdgeInsets.all(16),
                child: const Text(
                  'Cruelty-free brand',
                  style: TextStyle(fontSize: 20),
                ));
          }, childCount: 20))
        ],
      ),
    );
  }
}
