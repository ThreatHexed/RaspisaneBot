import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable
from enum import Enum

class Merger:
    """Represents a group of methods intended to merge a variety of different types of documents into a single output document.
    
    The specified input and output files or streams, along with the desired merge and save options,
    are used to merge the given input documents into a single output document.
    
    The merging functionality supports over 35 different file formats."""
    
    @overload
    @staticmethod
    def merge(output_file: str, input_files: list[str]) -> None:
        """Merges the given input documents into a single output document using specified input and output file names.
        
        :param output_file: The output file name.
        :param input_files: The input file names.
        
        By default :attr:`MergeFormatMode.KEEP_SOURCE_FORMATTING` is used."""
        ...
    
    @overload
    @staticmethod
    def merge(output_file: str, input_files: list[str], save_format: aspose.words.SaveFormat, merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> None:
        """Merges the given input documents into a single output document using specified input output file names and the final document format.
        
        :param output_file: The output file name.
        :param input_files: The input file names.
        :param save_format: The save format.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge(output_file: str, input_files: list[str], save_options: aspose.words.saving.SaveOptions, merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> None:
        """Merges the given input documents into a single output document using specified input output file names and save options.
        
        :param output_file: The output file name.
        :param input_files: The input file names.
        :param save_options: The save options.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge(input_files: list[str], merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> aspose.words.Document:
        """Merges the given input documents into a single document and returns :class:`aspose.words.Document` instance of the final document.
        
        :param input_files: The input file names.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge_stream(output_stream: io.BytesIO, input_streams: list[io.BytesIO], save_format: aspose.words.SaveFormat) -> None:
        """Merges the given input documents into a single output document using specified input output streams and the final document format.
        
        :param output_stream: The output stream.
        :param input_streams: The input streams.
        :param save_format: The save format."""
        ...
    
    @overload
    @staticmethod
    def merge_stream(output_stream: io.BytesIO, input_streams: list[io.BytesIO], save_options: aspose.words.saving.SaveOptions, merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> None:
        """Merges the given input documents into a single output document using specified input output streams and save options.
        
        :param output_stream: The output stream.
        :param input_streams: The input streams.
        :param save_options: The save options.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge_stream(input_streams: list[io.BytesIO], merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> aspose.words.Document:
        """Merges the given input documents into a single document and returns :class:`aspose.words.Document` instance of the final document.
        
        :param input_streams: The input streams.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    ...

class MergeFormatMode(Enum):
    """Specifies how formatting is merged when combining multiple documents."""
    
    """Combine the formatting of the merged documents.
    
    By using this option, Aspose.Words adapts the formatting of the first document to match the structure and
    appearance of the second document, but keeps some of the original formatting intact.
    This option is useful when you want to maintain the overall look and feel of the destination document
    but still retain certain formatting aspects from the original document.
    
    This option does not have any affect when the input and the output formats are PDF."""
    MERGE_FORMATTING: int
    
    """Means that the source document will retain its original formatting,
    such as font styles, sizes, colors, indents, and any other formatting elements applied to its content.
    
    By using this option, you ensure that the copied content appears as it did in the original source,
    regardless of the formatting settings of the first document in merge queue.
    
    This option does not have any affect when the input and the output formats are PDF."""
    KEEP_SOURCE_FORMATTING: int
    
    """Preserve the layout of the original documents in the final document.
    
    In general, it looks like you print out the original documents and manually adhere them together using glue."""
    KEEP_SOURCE_LAYOUT: int
    

