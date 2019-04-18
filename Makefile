CXX = g++
CFLAGS = -std=c++11 -Wall -Wextra -Werror
SRC = $(PWD)/src
BUILD = $(PWD)/build
OUT = $(PWD)/bin
MKDIR = mkdir -p

.PHONY: clean run all output

output: $(BUILD)/main.o $(BUILD)/detector.o | $(OUT)
	$(CXX) $(CFLAGS) $(BUILD)/main.o $(BUILD)/detector.o -o $(OUT)/pythondetector

$(OUT) $(BUILD):
	$(MKDIR) $@

$(BUILD)/main.o: $(BUILD)/detector.o | $(BUILD)
	$(CXX) -c $(SRC)/main.cpp -o $(BUILD)/main.o

$(BUILD)/detector.o: $(SRC)/detector.cpp | $(BUILD)
	$(CXX) -c $(SRC)/detector.cpp -o $(BUILD)/detector.o

clean:
	rm -rf $(BUILD) $(OUT)

run:
	$(OUT)/pythondetector